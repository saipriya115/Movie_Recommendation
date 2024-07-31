

# Create a directory for Streamlit configuration
mkdir -p ~/.streamlit/

# Create credentials file (example)


# Create Streamlit configuration file (example)
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
