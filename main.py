# Import necessary libraries
import streamlit as st
import tiktoken
from beartype import beartype


@beartype
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


# Create a Streamlit app
def main():
    st.title('Tiktoken Counter')

    encoding_name = "cl100k_base" 

    # Create a text area for user input
    user_input = st.text_area("Enter your text here\n(note that the counter is based on the cl100k_base encoding, used by GPT-3.5-Turbo and GPT-4)")

    # When there is user input
    if user_input:
        num_tokens = num_tokens_from_string(user_input, encoding_name=encoding_name)

        # Display the number of tokens
        st.write(f'Number of tokens: {num_tokens}')

if __name__ == "__main__":
    main()