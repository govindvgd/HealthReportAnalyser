import streamlit as st


def NavForAll():
    # st.image("/home/govind/coding/Hack/Plaksha Logo.png", width=50)
    st.write("""
    <style>
        .box:hover {
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
            text-decoration:none;
        }
        .dropdown-content a:hover {
            background-color: lightblue;
        }
        .next {
            display: grid;
            grid-template-columns: repeat(2, 100px);
            gap: 10px;
        }
    </style>
    
    <div style="height: 5vh;">
        <div id="my-element" style="color: white; width: 100%; background-color: grey; height: 50px; display: flex; justify-content: space-between; align-items: center; border: 2px solid black; border-radius: 5px;">
            <div class="dropdown" style="padding-left: 40px;">ABOUT DISEASES
                <div class="dropdown-content">
                    <a href="https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo7LrTeJB-YF0RNzx4PNSP8kQ4Su3WoI3-ebQly1gtgOlsYfhejmmuhoCx6UQAvD_BwE#tab=tab_1/">Diabetes</a>
                    <a href="https://www.cdc.gov/kidneydisease/basics.html#:~:text=CKD%20is%20a%20condition%20in,as%20heart%20disease%20and%20stroke.">Kidney Disease</a>
                    <a href="https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFoyHzJIf4JMBxGL3OJRkzF9Zxc3nb9v1RtM_-m7M3OuaYtrwWnbSVMBoCTNQQAvD_BwE">Heart Disease</a>
                    <a href="https://www.who.int/news-room/fact-sheets/detail/lung-cancer?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo6Dhr6irlDo0JuMysqzFEbtEuPxju4lC7OVPccqvDb785Db0L7AMYRoCbvUQAvD_BwE">Lung Cancer</a>
                    <a href="https://www.who.int/news-room/fact-sheets/detail/parkinson-disease#:~:text=Parkinson%20disease%20(PD)%20is%20a,muscle%20contractions%20and%20difficulty%20speaking.">Parkinson Disease</a>                                   
             </div>
            </div>
            <div style="display: flex; flex-direction: row; padding-right: 20px; justify-content: center;">
                <div class="box" style="margin-left:20px;padding: 10px;border-radius:9px">Home</div>
                <div class="box" style="margin-left:20px;padding: 10px;border-radius:9px">About us</div>
                <div class="box" style="margin-left:20px;padding: 10px;border-radius:9px">Disease info</div>
                <div class="box" style="margin-left:20px;padding: 10px;border-radius:9px">Login</div>
                <div class="box" style="margin-left:20px;padding: 10px;border-radius:9px">Contacts</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
