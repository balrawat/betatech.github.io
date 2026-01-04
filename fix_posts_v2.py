#!/usr/bin/env python3
"""
Enhanced script to improve formatting in all Jekyll posts
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
    content = re.sub(r'  \n', '\n', content)  # Remove trailing spaces before newlines
    
    # Fix escaped code blocks: `\# command` -> `# command`
    content = re.sub(r'`\\#', '`#', content)
    content = re.sub(r'`\\-', '`-', content)
    
    # Fix broken code blocks: `public`html_` -> `public_html`
    content = re.sub(r'`([^`]+)`([a-zA-Z_]+)`', r'`\1\2`', content)
    
    # Fix headings: **Heading**\n\n* * *\n\n -> ## Heading\n\n
    content = re.sub(r'\*\*([^*]+)\*\*\s*\n\s*\n\s*\* \* \*\s*\n\s*\n', r'## \1\n\n', content)
    
    # Fix headings without separators: **Heading**\n\n -> ## Heading\n\n
    content = re.sub(r'\*\*([^*]+)\*\*\s*\n\s*\n(?!\* \* \*)', r'## \1\n\n', content)
    
    # Fix numbered headings: "1. ## Heading" -> "### 1. Heading"
    content = re.sub(r'^(\d+)\.\s*##\s+', r'### \1. ', content, flags=re.MULTILINE)
    
    # Fix subheadings: **Step One—Title**\n\n* * * -> ### Step One—Title
    content = re.sub(r'\*\*Step ([^*]+)\*\*\s*\n\s*\n\s*\* \* \*', r'### Step \1', content)
    content = re.sub(r'\*\*([^*]+)—([^*]+)\*\*\s*\n\s*\n\s*\* \* \*', r'### \1—\2', content)
    content = re.sub(r'\*\*([^*]+)—([^*]+)\*\*\s*\n\s*\n(?!\* \* \*)', r'### \1—\2\n\n', content)
    
    # Fix empty headings: "### \n\n" -> remove
    content = re.sub(r'###\s+\n\s*\n', '', content)
    
    # Fix bullet points: · item -> - item
    content = re.sub(r'^·\s+', '- ', content, flags=re.MULTILINE)
    content = re.sub(r'^\\-\s+', '- ', content, flags=re.MULTILINE)
    content = re.sub(r'^-To\s+', '- To ', content, flags=re.MULTILINE)
    content = re.sub(r'^-disable\s+', '- Disable ', content, flags=re.MULTILINE)
    
    # Fix code blocks that are multiple lines
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
            is_code = any(x in inner for x in ['<', 'sudo', 'yum', 'apt', 'vi ', 'nano ', 'mkdir', 'chmod', 'chown', 'cd ', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls ', 'ps ', 'kill', 'service', 'systemctl', '#', '/etc/', '/var/', 'Protocol', 'Listen', 'VirtualHost', 'ServerAdmin', 'DocumentRoot', 'ServerName', 'PermitRootLogin', 'Banner', 'apachectl', 'httpd', 'sshd', 'ifconfig', 'nano'])
            
            if is_code:
                # Collect consecutive italic lines
                code_lines = []
                lang = 'bash'
                if '<' in inner:
                    lang = 'html'
                elif 'VirtualHost' in inner or 'ServerAdmin' in inner or 'Listen' in inner:
                    lang = 'apache'
                elif 'Protocol' in inner or 'PermitRootLogin' in inner or 'Banner' in inner or 'sshd' in inner:
                    lang = 'apache'  # SSH config is similar to apache format
                
                j = i
                while j < len(lines) and lines[j].strip().startswith('_') and lines[j].strip().endswith('_'):
                    code_line = lines[j].strip().strip('_').strip()
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
    
    # Fix standalone code commands that should be in code blocks
    # Pattern: lines with `command` that are commands
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        # Check if line is a standalone code command
        if re.match(r'^`[^`]+`$', line.strip()) and any(x in line for x in ['sudo', 'yum', 'apt', 'vi', 'nano', 'mkdir', 'chmod', 'chown', 'cd', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls', 'ps', 'kill', 'service', 'systemctl', '/etc/', '/var/']):
            # Check if next few lines are also commands
            code_lines = [line.strip().strip('`')]
            j = i + 1
            while j < len(lines) and j < i + 5:
                next_line = lines[j].strip()
                if re.match(r'^`[^`]+`$', next_line):
                    code_lines.append(next_line.strip('`'))
                    j += 1
                elif next_line == '':
                    j += 1
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
    
    # Clean up any remaining excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Fix link spacing: [text][ref] -> [text] [ref] (add space before link ref)
    content = re.sub(r'(\[([^\]]+)\])(\[[^\]]+\])', r'\1 \2', content)
    
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

