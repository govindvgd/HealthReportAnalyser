import streamlit as st

def welcome():

    st.write(
        """
        <style>
            .box:hover{
                background-color: lightblue;
            }
            .dropdown {
                position: relative;
                display: inline-block;
            }
            .dropdown-content {
                display: none;
                position: absolute;
                background-color: white;
                min-width: 220px;
                color: black;
                text-decoration: none;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
            }
            .dropdown:hover .dropdown-content {
                display: block;
            }
            .dropdown-content a {
                padding: 12px 16px;
                display: block;
                text-decoration: none;
                color: black; /* added to make the text black */
            }
            .dropdown-content a:hover {
                background-color: lightblue;
            }
            .next {
                display: grid;
                grid-template-columns: repeat(2, 100px); 
                gap: 10px;
            }
            .child {
                # background-color: lightblue;
            }
            .black-text {
                color: black;
            }
        </style>
             


<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text">🌟 Welcome to HealthReportAnalyzer! 🌟 </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">Your trusted ally in disease prediction and prevention. HealthGuardian is your go-to platform for state-of-the-art risk assessment solutions. Step into a world where proactive healthcare is the norm. Explore our innovative disease predictors below and take charge of your well-being today. Click below for Help and join the revolution in personalized healthcare! 🚀 </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">To know more </button>
    </div>
</div>
<br>





<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text"> Diabetes </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">"Diabetes, a chronic condition, results from inadequate insulin production or ineffective use of insulin by the body. Symptoms include frequent urination, increased thirst, and unexplained weight loss. Diagnosis relies on blood tests measuring blood sugar levels. Treatment involves lifestyle modifications, medication, and insulin therapy, highlighting the importance of regular monitoring and management." 🚀 </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;"><a href="https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFozaOzAZaq4C9gvq8UXYkUtkDTWYEoStZ3LVNxTSsKxhhDigNsiW6ShoC0wQQAvD_BwE#tab=tab_1" style="text-decoration:none;color:white;">To know more </a></button>
    </div>
</div>
<br>




<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text">Kidney Disease </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">"Kidney disease, a serious health condition, affects the vital organs responsible for filtering waste from the blood. Symptoms include fatigue, swelling, and changes in urination. Diagnosis often involves blood tests and imaging. Treatment varies from medication to dialysis or transplantation, emphasizing early detection and lifestyle management for optimal kidney health."🚀 </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;"><a href="https://www.cdc.gov/kidneydisease/basics.html#:~:text=CKD%20is%20a%20condition%20in,as%20heart%20disease%20and%20stroke./" style="text-decoration:none;color:white;">To know more</button>
    </div>
</div>
<br>





<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text">Heart Disease </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">"Heart disease, a leading cause of mortality globally, encompasses various conditions affecting the heart's function. Symptoms may include chest pain, shortness of breath, and fatigue. Diagnosis involves tests like EKG and angiography. Treatment ranges from lifestyle changes and medications to surgery, emphasizing prevention through healthy habits and regular medical check-ups."🚀 </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;"><a href="https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFoyHzJIf4JMBxGL3OJRkzF9Zxc3nb9v1RtM_-m7M3OuaYtrwWnbSVMBoCTNQQAvD_BwE" style="text-decoration:none;color:white;">To know more</button>
    </div>
</div>
<br>




<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text">Lung Cancer  </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">"Lung cancer, a deadly disease, develops when abnormal cells grow uncontrollably in the lungs. Symptoms may include persistent coughing, chest pain, and difficulty breathing. Diagnosis typically involves imaging tests like CT scans and biopsies. Treatment options include surgery, chemotherapy, and radiation therapy, with smoking cessation crucial for prevention and improved outcomes."🚀 </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;"><a href="https://www.niehs.nih.gov/health/topics/conditions/lung-disease" style="text-decoration:none;color:white;">To know more</button>
    </div>
</div>
<br>



<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text">Parkinson Disease </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">"Parkinson's disease, a neurodegenerative disorder, affects movement and coordination due to the loss of dopamine-producing brain cells. Symptoms include tremors, stiffness, and impaired balance. Diagnosis relies on clinical assessment and may involve imaging tests. Treatment includes medication, physical therapy, and sometimes surgery, focusing on symptom management and quality of life enhancement." </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;"><a href="https://www.who.int/news-room/fact-sheets/detail/parkinson-disease#:~:text=Parkinson%20disease%20(PD)%20is%20a,muscle%20contractions%20and%20difficulty%20speaking." style="text-decoration:none;color:white;">To know more</button>
    </div>
</div>
<br>






    """,
        unsafe_allow_html=True,
    )


def main():
    st.title("Welcome to my Streamlit App")
    welcome()


if __name__ == "__main__":
    main()