import json

with open('./test.json', 'r') as file:
    content = json.load(file)

textures = content.get("textures")
images = [
    "fcb84841eaf83ca051055d1f006dff2e2a2923.png",
    "11dd18e9468ac61659dee2a5dbdb0f34f6ad0e.png"
]


def search_index_with_cache(path):
    cache = {}
    def search():
        if cache.get(path) is not None:
            return cache.get(path)

        for indx, tex in enumerate(textures):
            tex_path = tex.get('path')
            if tex_path == path:
                return indx
            else:
                cache[tex_path] = indx
        return None
    return search()

def main():
    for image_path in images:
        index = search_index_with_cache(image_path)

main()