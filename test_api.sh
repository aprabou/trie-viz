#!/bin/bash

echo "🌳 Trie Visualizer Test Script"
echo "================================"

echo "📝 Testing word insertion..."
curl -X POST http://127.0.0.1:5000/insert \
  -H "Content-Type: application/json" \
  -d '{"word": "cat"}' \
  -s | python3 -m json.tool

echo ""
echo "📝 Testing another word insertion..."
curl -X POST http://127.0.0.1:5000/insert \
  -H "Content-Type: application/json" \
  -d '{"word": "car"}' \
  -s | python3 -m json.tool

echo ""
echo "🔍 Testing word search..."
curl -X POST http://127.0.0.1:5000/search \
  -H "Content-Type: application/json" \
  -d '{"word": "cat"}' \
  -s | python3 -m json.tool

echo ""
echo "🌳 Getting trie structure..."
curl -X GET http://127.0.0.1:5000/get_trie \
  -s | python3 -m json.tool

echo ""
echo "✅ Test completed! Visit http://127.0.0.1:5000 to see the visualization."
