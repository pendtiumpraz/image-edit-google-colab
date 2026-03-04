import glob, os

def run():
    for f in glob.glob('*.ipynb'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # We explicitly replace total_mem with total_memory
        if 'total_mem' in content:
            content = content.replace('total_mem', 'total_memory')
            # But wait, wait: in the vram() function, I had total_memory_ory if I ran replace twice?
            # Let's just fix it by cleanly replacing total_memory to X, then total_mem to total_memory, then X to total_memory
            content = content.replace('total_memory', 'total_mem') # reset any partial
            content = content.replace('total_mem', 'total_memory')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print("Fixed", f)
        else:
            print("Already fixed", f)

if __name__ == '__main__':
    run()
