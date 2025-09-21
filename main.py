from pyscript import document

def calculate_score(event):
    # html 
    scoreone = document.getElementById("scoreone").value
    scoretwo = document.getElementById("scoretwo").value

    # convert
    s1 = int(scoreone) if scoreone else 0
    s2 = int(scoretwo) if scoretwo else 0

    # calculate 
    compute = (s1 + s2) / 2

    # results if you passed or failed
    if compute >= 75:
        outcome = f"Average: {compute:.2f} ✅ Passed"
    else:
        outcome = f"Average: {compute:.2f} ❌ Failed"

    # show result 
    document.getElementById("compute").innerHTML = outcome