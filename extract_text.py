import streamlit as st 

file = st.file_uploader('Please upload your file')

def get_lines(upload_file):
	if upload_file is not None:
		content = upload_file.read().decode('utf-8').splitlines()
		st.write(len(content))
		for i in range(0, len(content)):
			if (i % 4 == 2):
				content[i]


result = get_lines(file)

st.write(result)

