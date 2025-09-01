# Trie Visualizer

A beautiful, interactive web application for visualizing Trie data structures with real-time search highlighting and Google-style design.

## 🚀 Live Demo

**Visit the live demo:** [https://aprabou.github.io/trie-viz/](https://aprabou.github.io/trie-viz/)

*The app is fully functional and works entirely in your browser - no backend required!*

## Features

- **🌳 Tree Visualization**: Beautiful tree-like visualization with each letter as a circular node
- **📝 Insert Words**: Add words to the trie by typing them in the input field
- **🔍 Real-time Search**: As you type in the search box, nodes are highlighted in real-time showing the path being traversed
- **🎯 Search Results**: Click search to see animated traversal and get detailed results:
  - ✅ Word found (complete word exists in trie)
  - 🔍 Prefix found (path exists but not a complete word)
  - ❌ Not found (path doesn't exist)
- **🎨 Interactive UI**: Modern, responsive design with smooth animations and color-coded nodes
- **🎭 Visual Feedback**: Different colors and animations for:
  - 🟣 Root node
  - 🔵 Regular nodes
  - 🟢 End-of-word nodes (complete words)
  - 🟡 Real-time highlighting while typing
  - 🟢 Search traversal animation

## How to Run Locally

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000`

## How to Use

1. **Inserting Words**: 
   - Type a word in the "Enter word to insert" field
   - Click "Insert Word" or press Enter
   - Watch the tree visualization update to show the new word structure

2. **Real-time Search**:
   - Start typing in the "Enter word to search" field
   - Watch as nodes light up in yellow showing the path being traversed
   - See immediate visual feedback for valid prefixes

3. **Complete Search**:
   - After typing, click "Search Word" or press Enter
   - Watch the animated green traversal through the tree
   - Get a detailed result showing whether it's a word, prefix, or not found

## Tree Visualization Legend

- **🟣 Purple ROOT**: The root node of the trie
- **🔵 Blue nodes**: Regular character nodes
- **🟢 Green nodes with thick border**: Complete words (end-of-word markers)
- **🟡 Yellow highlighting**: Real-time search path while typing
- **🟢 Green animation**: Final search traversal animation
- **Node labels**: Show the complete prefix up to that point

## Technical Details

- **Backend**: Flask with Python
- **Frontend**: Vanilla JavaScript with modern CSS animations
- **Data Structure**: Standard Trie implementation with prefix search
- **Visualization**: Tree layout with circular nodes and connecting lines
- **Real-time Updates**: Event-driven highlighting without page refreshes
- **Responsive Design**: Works on desktop and mobile devices

## API Endpoints

- `GET /` - Main application page
- `POST /insert` - Insert a word into the trie
- `POST /search` - Search for a word and get traversal path
- `GET /get_trie` - Get the current trie structure

## Example Usage

Try inserting words like:
- "cat", "car", "card" - to see branching
- "a", "an", "and" - to see nested structures
- "test", "testing", "tester" - to see word extensions
