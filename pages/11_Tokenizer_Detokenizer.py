import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')

# Streamlit app title
st.title("Tokenizer and Detokenizer using GPT-2 for 2D Canvas")
st.write("Example: cr8 lg cnvs html js hlds 9 wbs becomes 060980002300300000700026900077142592771144804002890033500082008600026601443")

# Tokenization section
st.header("Tokenization")
sentence = st.text_input("Enter a sentence to tokenize:", "cr8 lg cnvs html js hlds 9 wbs")

def format_token_ids(token_ids):
    formatted_ids = [str(token_id).zfill(5) for token_id in token_ids]
    return ''.join(formatted_ids)

if st.button("Tokenize"):
    input_ids = tokenizer(sentence, return_tensors='pt').input_ids
    token_ids_list = input_ids[0].tolist()
    formatted_token_ids = format_token_ids(token_ids_list)
    st.write("Tokenized input IDs (formatted):")
    st.write(formatted_token_ids)

# Detokenization section
st.header("Detokenization")
token_ids = st.text_input("Enter token IDs (concatenated without spaces):", "619710116000284001536")

def split_token_ids(concatenated_ids, length=5):
    return [concatenated_ids[i:i+length] for i in range(0, len(concatenated_ids), length)]

def remove_leading_zeros(grouped_ids):
    return [id.lstrip('0') for id in grouped_ids]

if st.button("Detokenize"):
    split_ids = split_token_ids(token_ids)
    cleaned_ids = remove_leading_zeros(split_ids)
    cleaned_token_ids_str = ' '.join(cleaned_ids)
    token_id_list = [int(id) for id in cleaned_ids if id.isdigit()]
    
    detokenized_sentence = tokenizer.decode(token_id_list)
    
    st.write("Grouped and cleaned token IDs:")
    st.write(cleaned_token_ids_str)
    st.write("Detokenized sentence:")
    st.write(detokenized_sentence)

# Load the model
gpt2 = AutoModelForCausalLM.from_pretrained('gpt2')

# Display help for the GPT-2 model
st.write("Help GPT2")
st.write(help(gpt2))