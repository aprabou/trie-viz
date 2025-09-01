# Trie Visualizer

A beautiful, interactive web application for visualizing Trie data structures with real-time search highlighting and Google-style design.

## 🌟 Features

- **Interactive Trie Building**: Insert words by typing and see the trie structure grow
- **Real-time Search**: Search for words with animated path traversal
- **Visual Feedback**: Different colors and animations for:
  - Search path highlighting
  - Word completion indicators
  - Traversal animations
- **Delete Functionality**: Remove prefixes and their children with confirmation dialogs
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Toast Notifications**: Elegant slide-in notifications for user feedback
- **Google-inspired UI**: Clean, modern interface using Google's color palette

## 🚀 Live Demo

Visit the live demo: [https://aprabou.github.io/trie-viz/](https://aprabou.github.io/trie-viz/)

## 🛠️ How to Use

1. **Insert Words**: Type a word in the "Enter word to insert" field and click "Insert Word" or press Enter
2. **Search Words**: Type in the search field to see real-time highlighting, or click "Search Trie" for animated traversal
3. **Delete Prefixes**: Hover over any node and click the red × button to delete that prefix and all its children
4. **Visual Indicators**:
   - **Purple nodes**: Root of the trie
   - **Green nodes**: Complete words (end of word markers)
   - **Blue nodes**: Regular prefix nodes
   - **Orange highlighting**: Real-time search path
   - **Green animation**: Final search traversal

## 🔧 Technologies Used

- **Pure JavaScript**: Client-side trie implementation
- **HTML5 & CSS3**: Modern web standards with animations
- **Responsive Design**: Flexbox and CSS Grid for perfect layouts
- **No Dependencies**: Runs entirely in the browser

## 📁 Project Structure

```
trie-viz/
├── docs/
│   └── index.html          # Standalone GitHub Pages version
├── templates/
│   └── index.html          # Flask template version
├── app.py                  # Flask backend (for local development)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🏗️ Local Development

### Option 1: Static Version (GitHub Pages)
Simply open `docs/index.html` in your browser. No setup required!

### Option 2: Flask Version (with Python backend)
```bash
# Clone the repository
git clone https://github.com/aprabou/trie-viz.git
cd trie-viz

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Then open http://localhost:5000 in your browser.

## 🚀 GitHub Pages Deployment

This project is automatically deployed to GitHub Pages from the `docs/` folder. Any changes to `docs/index.html` will be automatically reflected on the live site.

To deploy your own version:

1. Fork this repository
2. Go to your repository settings
3. Scroll to "Pages" section
4. Select "Deploy from a branch"
5. Choose "main" branch and "/docs" folder
6. Your site will be available at `https://yourusername.github.io/trie-viz/`

## 🎨 Design Features

- **Google Color Palette**: Uses authentic Google colors (#4285f4, #ea4335, #fbbc05, #34a853)
- **Smooth Animations**: CSS transitions and keyframe animations
- **Toast Notifications**: Slide-in notifications from the right side
- **Custom Modal Dialogs**: In-page confirmation dialogs instead of browser popups
- **Mobile Responsive**: Optimized for all screen sizes
- **Accessibility**: Keyboard navigation and screen reader friendly

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by Google's clean design philosophy
- Built for educational purposes to help visualize trie data structures
- Thanks to the open source community for inspiration and tools

---

Made with ❤️ for computer science education
