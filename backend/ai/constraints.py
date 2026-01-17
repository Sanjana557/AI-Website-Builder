def build_constraints(data):
    return f"""
    Website Type: {data['website_type']}
    Brand Tone: {data['tone']}
    Color Scheme: {data['color']}
    Required Sections: {', '.join(data['sections'])}
    Must be mobile responsive.
    Use modern, clean UI patterns.
    """
