import markdown

def render_markdown(input_string):
    html = markdown.markdown(input_string)
    return html
