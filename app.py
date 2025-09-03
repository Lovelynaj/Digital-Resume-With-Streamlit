# Used / Installed packages are, streamlit, Pillow, pipreqs

from pathlib import Path
from PIL import Image
import streamlit as st

# PATH SETTINGS to locate the files
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"

# GENERAL SETTINGS
PAGE_TITLE = "Digital CV | Lovely Naj"
PAGE_ICON = ":wave:"
NAME = "Lovely Naj"
DESCRIPTION = """
FullStack Web Developer, @C4Wdesign, CEO & Manager, Creating, Designing and Developing Professional Websites 
"""
EMAIL = "info@c4wdesign.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@NajiTech360",
    "Github": "https://github.com/Lovelynaj",
    "Linkedin": "https://www.linkedin.com/in/husainnajeeb/",
    "C4Wdesign": "https://www.c4wdesign.com"
}

PROJECTS = {
    "🏆 Digital CV - HTML-CSS deployed on Github": "https://lovelynaj.github.io/najeeb_CV_2024_updated/",
    "🏆 Agency Website - WordPress Web Design": "https://c4wdesign.com",
    "🏆 Digital CV - HTML Only": "https://lovelynaj.github.io/cv/",
    "🏆 How to create a Youtube Channel 2023": "https://www.youtube.com/watch?v=az7nLOea_gQ&t=279s"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# LOAD CSS, PDF AND PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),
                unsafe_allow_html=True)  # Helps to apply custom css

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Load the profile_picture
profile_pic = Image.open(profile_pic)


# CREATING A HERO SECTION
col1, col2 = st.columns(2, gap="small")  # 2 columns with small gap
with col1:
    st.image(profile_pic, width=260)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    st.write("📧", EMAIL)


# SOCIAL LINKS
# the hash or pound sign add empty spaces similar to break <br> in html
st.write("---")
# to determine how many columns needed, we can count using len()
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    # this loops and show all my SOCIAL_MEDIA LINKS
    cols[index].write(f"[{platform}]({link})")

st.write("---")

# EDUCATION
st.subheader("🎓 Education")
st.write("💻 IFCD0210 App Development with Web Tech. | CoreNetworks.es **2024** | Madrid")
st.write("🖥️ IFCT127PO Big Data Architecture | CoreNetworks.es **2024** | Madrid")
st.write("🎓 Msc. Material Eng. (Erasmus) | UPM | **2022 - 2023** | Madrid")
st.write("📗 BSc. Material Eng. | Mugla Sitki Kocman University | **2014 - 2019** | TURKEY")


# EXPERIENCE AND QUALIFICATION
# if you add a dash - in front of a sentence, streamlit understood it as an ordered list
st.write("---")
st.subheader("🏆 Experience & Qualifications")
st.write(
    """
    - ✅ Designed & developed responsive websites using HTML, CSS, & JavaScript.
    - ✅ Best in WordPress theme modification, plugin integration, & SEO optimization.
    - ✅ Created modern user-friendly UI/UX layouts.
    - ✅ Deployed & maintained websites on hosting platforms, ensuring speed, & security.
"""
)

# SKILLS
st.write("---")
st.subheader("🔑 Key Skills")
st.write(
    """
    - 👨‍💻 Proficient in HTML, CSS, JavaScript, React, Python, WordPress.
    - 📑 Strong knowledge of SEO, digital marketing, and content optimization.
    - 📊 Skilled in graphic design tools (Canva, Photoshop) creating engaging visuals.
    - 🤝 Ability to manage projects, communicate with clients, and deliver on deadlines.
"""
)


# WORK HISTORY
st.write("---")
st.subheader("🛍️ Work History")
# st.write("---")  # adding divider --- adds a divider

# JOB 1
st.write("💻", "**Graphic & Web Designer | C4Wdesign**")
st.write("2019 - 2024")
st.write(
    """
    - ▶️ Design a website for clients internationally. (E-commerce, agency, portfolio, etc.)
    - ▶️ Help clients solve their website issues
    - ▶️ Edit images for clients
    - ▶️ Create brochures, flyers, certificates, logos, mock-ups, etc.
"""
)


# JOB 2
st.write("💻", "**Computer & Phone Technician| Udemy**")
st.write("2023 - 2024")
st.write(
    """
    - ▶️ Install, maintain and repair basic mobile/computers and networks effectively
    - ▶️ Device diagnostics, Software Updates
    - ▶️ Problem-solving
"""
)


# PROJECTS & ACCOMPLISHMENTS
st.write("---")
st.subheader("👨‍💻 Projects & Accomplishments")
for project, link in PROJECTS.items():
    # this will derive only the links I have in my projects and display them
    st.write(f"[{project}]({link})")
