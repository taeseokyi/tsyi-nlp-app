mkdir -p ~/.streamlit/

echo "
[server]
port = $PORT
enableCORS = false

" > ~/.streamlit/config.toml
