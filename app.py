import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Shubham - Data Scientist Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        color: #1565C0;
        border-bottom: 3px solid #1E88E5;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .skill-tag {
        background-color: #E3F2FD;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        display: inline-block;
        font-weight: 500;
    }
    .project-card {
        background-color: #FAFAFA;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1E88E5;
        margin-bottom: 1rem;
    }
    .stat-box {
        background: linear-gradient(135deg, #1E88E5, #1565C0);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    .contact-info {
        font-size: 1.1rem;
        padding: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "👤 About", "💼 Skills", "📁 Projects", "📝 Experience", "🎓 Education", "📞 Contact"]
)

# Home Page
if page == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<p class="main-header">Shubham</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Data Scientist | Machine Learning Enthusiast</p>', unsafe_allow_html=True)
        
        # Profile image placeholder
        try:
            st.image("image.png", width=200)
        except:
            st.markdown("### 👤", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Quick Stats
        col_a, col_b, col_c, col_d = st.columns(4)
        with col_a:
            st.markdown('<div class="stat-box"><h3>5+</h3><p>Years Experience</p></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="stat-box"><h3>20+</h3><p>Projects Completed</p></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div class="stat-box"><h3>15+</h3><p>Models Deployed</p></div>', unsafe_allow_html=True)
        with col_d:
            st.markdown('<div class="stat-box"><h3>10+</h3><p>Publications</p></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🚀 Quick Links")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📁 View Projects", use_container_width=True)
        with col2:
            st.button("📄 Download Resume", use_container_width=True)
        with col3:
            st.button("📞 Contact Me", use_container_width=True)

# About Page
elif page == "👤 About":
    st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Hello! I'm Shubham 👋
        
        A passionate **Data Scientist** with expertise in turning complex data into actionable insights. 
        I specialize in building machine learning models, performing statistical analysis, and creating 
        data-driven solutions that solve real-world problems.
        
        My journey in data science began with a fascination for how data can tell stories and drive decisions. 
        Since then, I've worked on diverse projects ranging from predictive analytics to natural language processing.
        
        ### 🎯 What I Do
        - **Data Analysis & Visualization**: Transforming raw data into meaningful insights
        - **Machine Learning**: Building predictive models for classification, regression, and clustering
        - **Deep Learning**: Implementing neural networks for complex tasks
        - **Data Engineering**: Creating pipelines for data processing and model deployment
        """)
    
    with col2:
        st.markdown("### 📍 Location")
        st.info("India")
        st.markdown("### 💼 Status")
        st.success("Open to Opportunities")
        st.markdown("### 🌐 Languages")
        st.write("English, Hindi")

# Skills Page
elif page == "💼 Skills":
    st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        st.markdown("""
        <span class="skill-tag">🐍 Python</span>
        <span class="skill-tag">🐼 Pandas</span>
        <span class="skill-tag">NumPy</span>
        <span class="skill-tag">R Programming</span>
        <span class="skill-tag">SQL</span>
        """, unsafe_allow_html=True)
        
        st.markdown("### Machine Learning")
        st.markdown("""
        <span class="skill-tag">Scikit-learn</span>
        <span class="skill-tag">TensorFlow</span>
        <span class="skill-tag">PyTorch</span>
        <span class="skill-tag">Keras</span>
        <span class="skill-tag">XGBoost</span>
        <span class="skill-tag">LightGBM</span>
        """, unsafe_allow_html=True)
        
        st.markdown("### Deep Learning")
        st.markdown("""
        <span class="skill-tag">Neural Networks</span>
        <span class="skill-tag">CNN</span>
        <span class="skill-tag">RNN/LSTM</span>
        <span class="skill-tag">Transformers</span>
        <span class="skill-tag">Computer Vision</span>
        <span class="skill-tag">NLP</span>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Data Visualization")
        st.markdown("""
        <span class="skill-tag">📊 Matplotlib</span>
        <span class="skill-tag">📈 Seaborn</span>
        <span class="skill-tag">📉 Plotly</span>
        <span class="skill-tag">Tableau</span>
        <span class="skill-tag">Power BI</span>
        """, unsafe_allow_html=True)
        
        st.markdown("### Tools & Platforms")
        st.markdown("""
        <span class="skill-tag">Jupyter</span>
        <span class="skill-tag">Git/GitHub</span>
        <span class="skill-tag">Docker</span>
        <span class="skill-tag">AWS</span>
        <span class="skill-tag">Google Cloud</span>
        <span class="skill-tag">MLflow</span>
        """, unsafe_allow_html=True)
        
        st.markdown("### Databases")
        st.markdown("""
        <span class="skill-tag">MySQL</span>
        <span class="skill-tag">PostgreSQL</span>
        <span class="skill-tag">MongoDB</span>
        <span class="skill-tag">Redis</span>
        """, unsafe_allow_html=True)
    
    # Skill Progress Bars
    st.markdown("### 📊 Proficiency Levels")
    skill_data = {
        "Python": 95,
        "Machine Learning": 90,
        "Deep Learning": 85,
        "Data Visualization": 88,
        "SQL": 85,
        "Statistics": 90
    }
    
    for skill, level in skill_data.items():
        st.markdown(f"**{skill}**")
        st.progress(level/100, text=f"{level}%")

# Projects Page
elif page == "📁 Projects":
    st.markdown('<p class="section-header">Featured Projects</p>', unsafe_allow_html=True)
    
    # Project filters
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        filter_option = st.selectbox("Filter by Category", ["All", "Machine Learning", "Deep Learning", "Data Analysis", "NLP"])
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>🏥 Customer Churn Prediction</h3>
        <p><strong>Category:</strong> Machine Learning | <strong>Tech:</strong> Python, Scikit-learn, XGBoost</p>
        <p>Built a predictive model to identify customers likely to churn with 92% accuracy. 
        Implemented feature engineering and hyperparameter tuning for optimal performance.</p>
        <p>🔗 <a href="#">View Code</a> | 📦 <a href="#">Live Demo</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>📰 Sentiment Analysis System</h3>
        <p><strong>Category:</strong> NLP | <strong>Tech:</strong> Python, TensorFlow, BERT, Transformers</p>
        <p>Developed a real-time sentiment analysis system for social media posts using transformer-based 
        models. Achieved 94% accuracy on benchmark datasets.</p>
        <p>🔗 <a href="#">View Code</a> | 📦 <a href="#">Live Demo</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3
    st.markdown("""
    <div class="project-card">
        <h3>🖼️ Image Classification for Medical Imaging</h3>
        <p><strong>Category:</strong> Deep Learning | <strong>Tech:</strong> Python, PyTorch, CNN, OpenCV</p>
        <p>Created a CNN model for classifying medical images with 96% accuracy. 
        Used transfer learning and data augmentation techniques.</p>
        <p>🔗 <a href="#">View Code</a> | 📦 <a href="#">Live Demo</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 4
    st.markdown("""
    <div class="project-card">
        <h3>📊 Sales Forecasting Dashboard</h3>
        <p><strong>Category:</strong> Data Analysis | <strong>Tech:</strong> Python, Pandas, Streamlit, Plotly</p>
        <p>Built an interactive dashboard for visualizing and forecasting sales data using time series analysis. 
        Integrated multiple visualization techniques for comprehensive insights.</p>
        <p>🔗 <a href="#">View Code</a> | 📦 <a href="#">Live Demo</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 5
    st.markdown("""
    <div class="project-card">
        <h3>🤖 Recommendation System</h3>
        <p><strong>Category:</strong> Machine Learning | <strong>Tech:</strong> Python, Surprise, Collaborative Filtering</p>
        <p>Developed a hybrid recommendation system for an e-commerce platform. 
        Improved user engagement by 35% through personalized recommendations.</p>
        <p>🔗 <a href="#">View Code</a> | 📦 <a href="#">Live Demo</a></p>
    </div>
    """, unsafe_allow_html=True)

# Experience Page
elif page == "📝 Experience":
    st.markdown('<p class="section-header">Work Experience</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 💼 Data Scientist
    **Tech Corporation** | *2022 - Present*
    - Led development of ML models for customer behavior prediction
    - Improved model accuracy by 25% through feature engineering
    - Mentored junior data scientists and conducted workshops
    - Collaborated with cross-functional teams to deploy ML solutions
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🔬 Data Analyst
    **Data Solutions Inc.** | *2020 - 2022*
    - Performed exploratory data analysis on large datasets
    - Created automated reporting dashboards using Tableau
    - Conducted statistical analysis to support business decisions
    - Reduced data processing time by 40% through optimization
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📈 Junior Data Scientist
    **Startup XYZ** | *2019 - 2020*
    - Built initial ML models for product recommendation
    - Implemented data pipelines for real-time processing
    - Developed visualization tools for stakeholders
    - Participated in hackathons and innovation challenges
    """)

# Education Page
elif page == "🎓 Education":
    st.markdown('<p class="section-header">Education & Certifications</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎓 Academic Education
        """)
        st.markdown("""
        **Master of Technology in Data Science**
        - Indian Institute of Technology (IIT)
        - *2018 - 2020*
        - Specialization in Machine Learning & AI
        - Thesis: "Deep Learning Approaches for Time Series Forecasting"
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Bachelor of Technology in Computer Science**
        - National Institute of Technology (NIT)
        - *2014 - 2018*
        - Focus on Algorithms and Database Systems
        - CGPA: 8.5/10
        """)
    
    with col2:
        st.markdown("### 🏆 Key Achievements")
        st.success("✓ Gold Medalist in M.Tech")
        st.success("✓ Best Paper Award at ICML 2020")
        st.success("✓ Kaggle Competition Winner (Top 1%)")
        st.success("✓ Published 5+ Research Papers")
    
    st.markdown("---")
    
    st.markdown("### 📜 Professional Certifications")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.info("🧠 Deep Learning Specialization - Coursera")
    with col_b:
        st.info("📊 Google Data Analytics Professional")
    with col_c:
        st.info("🔧 AWS Machine Learning Specialty")

# Contact Page
elif page == "📞 Contact":
    st.markdown('<p class="section-header">Get In Touch</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📧 Contact Information")
        st.markdown("""
        <p class="contact-info">📧 <strong>Email:</strong> shubham.datascientist@email.com</p>
        <p class="contact-info">📱 <strong>Phone:</strong> +91 98765 43210</p>
        <p class="contact-info">📍 <strong>Location:</strong> India</p>
        <p class="contact-info">💼 <strong>LinkedIn:</strong> linkedin.com/in/shubhamds</p>
        <p class="contact-info">🐙 <strong>GitHub:</strong> github.com/shubhamds</p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📝 Send a Message")
        with st.form(key="contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=100)
            submit = st.form_submit_button("Send Message ✉️")
            
            if submit:
                st.success("Thank you for your message! I'll get back to you soon.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Built with ❤️ using Streamlit | © 2024 Shubham</p>
    <p>Let's connect and create something amazing together!</p>
</div>
""", unsafe_allow_html=True)
