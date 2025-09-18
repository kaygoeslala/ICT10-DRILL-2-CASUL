from pyscript import when, display, document, HTML

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    profile_html = f"""
    <div class="card">
        <h3>✧ Student Profile ✧</h3>
        <p><b>Name:</b> {name}</p>
        <p><b>Age:</b> {age}</p>
        <p><b>School:</b> {school}</p>
        <div class="note">
            🌸 {name} is {age} years old and studies at {school}. 
        </div>
    </div>
    """

    document.querySelector("#output").innerHTML = ""
    display(HTML(profile_html), target="output")

