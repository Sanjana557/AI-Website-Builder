def generate_site(prompt: str):
    p = prompt.lower()

    # -------- COLOR SYSTEM ----------
    if "blue" in p:
        bg = "#0f172a"; accent = "#3b82f6"
    elif "purple" in p:
        bg = "#1e003a"; accent = "#a855f7"
    elif "green" in p:
        bg = "#052e16"; accent = "#22c55e"
    elif "orange" in p:
        bg = "#3b1d00"; accent = "#fb923c"
    else:
        bg = "#111827"; accent = "#38bdf8"

    # -------- TONE SYSTEM ----------
    if "minimal" in p:
        radius = "4px"; shadow = "none"; anim = "none"
    elif "bold" in p:
        radius = "18px"; shadow = "0 10px 30px rgba(0,0,0,0.5)"; anim = "transform:scale(1.05);"
    else:  # modern
        radius = "12px"; shadow = "0 6px 20px rgba(0,0,0,0.3)"; anim = "transform:translateY(-10px);"

    # -------- WEBSITE TYPE ----------
    if "portfolio" in p:
        title = "Creative Portfolio"
        sections = ["Projects", "Skills", "Experience"]
    elif "e-commerce" in p:
        title = "Online Store"
        sections = ["Products", "Offers", "Cart"]
    else:
        title = "Business Website"
        sections = ["Services", "Clients", "Contact"]

    cards = "".join(
        [f"<div class='card'>{s}</div>" for s in sections]
    )

    return f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {{
  margin:0; background:{bg}; color:white; font-family:Arial;
}}
nav {{
  padding:20px 40px; background:black; display:flex; justify-content:space-between;
}}
.hero {{
  padding:80px 40px; text-align:center;
}}
.hero h1 {{ color:{accent}; }}
.grid {{
  display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
  gap:30px; padding:40px;
}}
.card {{
  background:rgba(255,255,255,0.08);
  padding:35px; border-radius:{radius};
  box-shadow:{shadow};
  transition:0.3s;
}}
.card:hover {{{anim}}}
</style>
</head>
<body>

<nav><h2>{title}</h2><div>Home | About | Contact</div></nav>

<section class="hero">
<h1>{title}</h1>
<p>{prompt}</p>
</section>

<section class="grid">
{cards}
</section>

</body>
</html>
"""
