from flask import Flask, render_template, request, jsonify
import json

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word:
            current = self.root

            for c in word:
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
            
            current.endOfWord = True

    def search(self, word):
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        
        return current.endOfWord

    def startsWith(self, prefix):
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        
        return True

    def delete_prefix(self, prefix):
        """Delete a prefix and all its children from the trie"""
        if not prefix:
            # Clear the entire trie if root is deleted
            self.root.children.clear()
            self.root.endOfWord = False
            return True
        
        def delete_node(node, prefix, index):
            if index == len(prefix):
                # Found the node to delete - clear all children and mark as not end of word
                node.children.clear()
                node.endOfWord = False
                return True
            
            char = prefix[index]
            if char not in node.children:
                return False
            
            # Recursively find and delete
            deleted = delete_node(node.children[char], prefix, index + 1)
            
            if deleted and index == len(prefix) - 1:
                # This is the parent of the deleted node
                # Remove the child if it has no children and is not end of word
                child_node = node.children[char]
                if not child_node.children and not child_node.endOfWord:
                    del node.children[char]
            
            return deleted
        
        return delete_node(self.root, prefix, 0)

    def get_search_path(self, word):
        """Get the path traversed when searching for a word"""
        path = []
        current = self.root
        current_path = ""

        for c in word:
            current_path += c
            if c not in current.children:
                break
            current = current.children[c]
            path.append({
                'prefix': current_path,
                'found': True,
                'endOfWord': current.endOfWord
            })
        
        return path

    def to_dict(self):
        """Convert trie to dictionary for visualization"""
        def node_to_dict(node, prefix=""):
            result = {
                'prefix': prefix,
                'endOfWord': node.endOfWord,
                'children': {}
            }
            
            for char, child in node.children.items():
                result['children'][char] = node_to_dict(child, prefix + char)
            
            return result
        
        return node_to_dict(self.root)

app = Flask(__name__)
trie = Trie()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_word():
    data = request.get_json()
    word = data.get('word', '').lower().strip()
    
    if word:
        trie.insert(word)
        return jsonify({
            'success': True,
            'message': f'Word "{word}" inserted successfully',
            'trie_data': trie.to_dict()
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Please enter a valid word'
        })

@app.route('/search', methods=['POST'])
def search_word():
    data = request.get_json()
    word = data.get('word', '').lower().strip()
    
    if word:
        found = trie.search(word)
        path = trie.get_search_path(word)
        
        return jsonify({
            'success': True,
            'found': found,
            'path': path,
            'word': word
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Please enter a word to search'
        })

@app.route('/delete', methods=['POST'])
def delete_prefix():
    data = request.get_json()
    prefix = data.get('prefix', '').lower().strip()
    
    success = trie.delete_prefix(prefix)
    if success:
        if not prefix:
            message = 'Entire trie cleared successfully'
        else:
            message = f'Prefix "{prefix}" and all its children deleted successfully'
        
        return jsonify({
            'success': True,
            'message': message,
            'trie_data': trie.to_dict()
        })
    else:
        return jsonify({
            'success': False,
            'message': f'Prefix "{prefix}" not found in trie'
        })

@app.route('/get_trie', methods=['GET'])
def get_trie():
    return jsonify({
        'trie_data': trie.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)
