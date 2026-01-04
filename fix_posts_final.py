#!/usr/bin/env python3
"""
Final script to properly format all Jekyll posts
"""
import re
import os
import glob

def fix_post_formatting(content):
    """Fix common formatting issues in posts"""
    
    # Fix image format: [![](url)][ref] -> ![alt](url)  
    content = re.sub(r'\[!\[\]\(([^)]+)\)\]\[[^\]]+\]', r'![](\1)', content)
    
    # Remove excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'  \n', '\n', content)
    
    # Fix escaped characters in code blocks
    content = re.sub(r'`\\#', '`#', content)
    content = re.sub(r'`\\-', '`-', content)
    
    # Fix broken code blocks with backticks in the middle
    content = re.sub(r'`([^`]+)`([a-zA-Z_]+)`', r'`\1\2`', content)
    
    # Fix headings: **Heading**\n\n* * *\n\n -> ## Heading\n\n
    content = re.sub(r'\*\*([^*]+)\*\*\s*\n\s*\n\s*\* \* \*\s*\n\s*\n', r'## \1\n\n', content)
    
    # Fix headings without separators but with bold: **Heading**\n\n -> ## Heading\n\n
    # But only if it's at start of line or after blank line
    content = re.sub(r'(^|\n\n)\*\*([^*]+)\*\*\s*\n\s*\n(?!\* \* \*)', r'\1## \2\n\n', content, flags=re.MULTILINE)
    
    # Fix numbered headings: "1. ## Heading" -> "### 1. Heading"
    content = re.sub(r'^(\d+)\.\s*##\s+', r'### \1. ', content, flags=re.MULTILINE)
    
    # Fix subheadings with dashes: **Step One—Title**\n\n* * * -> ### Step One—Title
    content = re.sub(r'\*\*Step ([^*]+)\*\*\s*\n\s*\n\s*\* \* \*', r'### Step \1', content)
    content = re.sub(r'\*\*([^*]+)—([^*]+)\*\*\s*\n\s*\n\s*\* \* \*', r'### \1—\2', content)
    content = re.sub(r'\*\*([^*]+)—([^*]+)\*\*\s*\n\s*\n(?!\* \* \*)', r'### \1—\2\n\n', content)
    
    # Fix empty headings
    content = re.sub(r'###\s+\n\s*\n', '', content)
    
    # Fix bullet points
    content = re.sub(r'^·\s+', '- ', content, flags=re.MULTILINE)
    content = re.sub(r'^\\-\s+', '- ', content, flags=re.MULTILINE)
    content = re.sub(r'^-To\s+', '- To ', content, flags=re.MULTILINE)
    content = re.sub(r'^-disable\s+', '- Disable ', content, flags=re.MULTILINE)
    content = re.sub(r'^-([a-z])', lambda m: '- ' + m.group(1).upper(), content, flags=re.MULTILINE)
    
    # Fix multi-line italic code blocks (HTML, config files, etc.)
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if this looks like start of italic code block
        if stripped.startswith('_') and stripped.endswith('_') and len(stripped) > 2:
            inner = stripped[1:-1].strip()
            # Determine if it's code
            is_code = any(x in inner for x in ['<', 'sudo', 'yum', 'apt', 'vi ', 'nano ', 'mkdir', 'chmod', 'chown', 'cd ', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls ', 'ps ', 'kill', 'service', 'systemctl', '#', '/etc/', '/var/', 'Protocol', 'Listen', 'VirtualHost', 'ServerAdmin', 'DocumentRoot', 'ServerName', 'PermitRootLogin', 'Banner', 'apachectl', 'httpd', 'sshd', 'ifconfig', 'nano', 'Protocol', 'PermitRootLogin', 'Banner', 'ServerAlias', 'ErrorLog', 'CustomLog'])
            
            if is_code:
                # Collect consecutive italic lines
                code_lines = []
                lang = 'bash'
                if '<' in inner:
                    lang = 'html'
                elif any(x in inner for x in ['VirtualHost', 'ServerAdmin', 'Listen', 'NameVirtualHost', 'ServerAlias', 'ErrorLog', 'CustomLog']):
                    lang = 'apache'
                elif any(x in inner for x in ['Protocol', 'PermitRootLogin', 'Banner', 'sshd']):
                    lang = 'apache'  # SSH config format
                
                j = i
                while j < len(lines) and lines[j].strip().startswith('_') and lines[j].strip().endswith('_'):
                    code_line = lines[j].strip().strip('_').strip()
                    # Remove escape characters
                    code_line = code_line.replace('\\#', '#').replace('\\-', '-')
                    code_lines.append(code_line)
                    j += 1
                
                if len(code_lines) > 1 or (len(code_lines) == 1 and len(code_lines[0]) > 15):
                    # It's a code block
                    result.append('```' + lang)
                    result.extend(code_lines)
                    result.append('```')
                    i = j
                    continue
        
        result.append(line)
        i += 1
    
    content = '\n'.join(result)
    
    # Fix standalone commands that should be in code blocks
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if line is a standalone code command
        if re.match(r'^`[^`]+`$', stripped):
            cmd = stripped.strip('`').strip()
            # Check if it's a command (not just a word)
            is_command = any(x in cmd for x in ['sudo', 'yum', 'apt', 'vi', 'nano', 'mkdir', 'chmod', 'chown', 'cd ', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls ', 'ps ', 'kill', 'service', 'systemctl', '/etc/', '/var/', 'apachectl', 'httpd', 'sshd', 'ifconfig'])
            
            if is_command and len(cmd) > 5:
                # Check if next few lines are also commands
                code_lines = [cmd]
                j = i + 1
                consecutive_commands = 0
                
                while j < len(lines) and j < i + 10:
                    next_line = lines[j].strip()
                    if next_line == '':
                        j += 1
                        if consecutive_commands > 0:
                            break
                        continue
                    elif re.match(r'^`[^`]+`$', next_line):
                        next_cmd = next_line.strip('`').strip()
                        if any(x in next_cmd for x in ['sudo', 'yum', 'apt', 'vi', 'nano', 'mkdir', 'chmod', 'chown', 'cd ', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls ', 'ps ', 'kill', 'service', 'systemctl', '/etc/', '/var/']):
                            code_lines.append(next_cmd)
                            consecutive_commands += 1
                            j += 1
                        else:
                            break
                    else:
                        break
                
                if len(code_lines) > 1:
                    result.append('```bash')
                    result.extend(code_lines)
                    result.append('```')
                    i = j
                    continue
        
        result.append(line)
        i += 1
    
    content = '\n'.join(result)
    
    # Clean up excessive blank lines again
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Fix spacing around links
    content = re.sub(r'(\[([^\]]+)\])(\[[^\]]+\])', r'\1 \2', content)
    
    # Fix spacing: "text[link]" -> "text [link]"
    content = re.sub(r'([a-zA-Z0-9])(\[)', r'\1 \2', content)
    
    return content

def process_all_posts():
    """Process all markdown files in _posts directory"""
    posts_dir = '_posts'
    if not os.path.exists(posts_dir):
        print(f"Directory {posts_dir} not found!")
        return
    
    md_files = glob.glob(os.path.join(posts_dir, '*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    fixed_count = 0
    for filepath in sorted(md_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixed_content = fix_post_formatting(content)
            
            if fixed_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                fixed_count += 1
                print(f"Fixed: {os.path.basename(filepath)}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    process_all_posts()

