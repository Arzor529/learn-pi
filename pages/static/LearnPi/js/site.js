//Learn Pi Custom JS - Aaron Keel

//Quiz Related JS

//function to display chosen checkbox value in 'coding' window beside the quiz.

    //These ids are passed in the template and are the ids of the relevant django models holding the quiz data
    function displayRadioValue(questionID, answerID) {
        //stores chosen checkbox value in quizAnswer variable and uses answerID to uniquely identify the checkbox value
        var quizAnswer = document.getElementById("quizAnswer" + answerID).value;
        //locates the relevant <p> tag created for each question and places the checkbox value into it
        document.getElementById("quiz-question" + questionID).innerHTML = quizAnswer; 
        document.getElementById("quiz-question" + questionID).style.backgroundColor = "aliceblue";
    }

    function submitQuiz() {
        //get the Elements object of all radio buttons and store it in a variable
        var submittedAnswers = document.getElementsByClassName('quizQuestion');
        //create an array to store the question Correct Boolean
        checkedArr = [];
        //loop through every item in the submittedAnswers object
        for (var i = 0; i < submittedAnswers.length; ++i) {
            //if the radio button is checked, push the tag attribute value which stores the question correct
            //boolean to the checkedArr array
            if (submittedAnswers[i].checked) {
                checkedArr.push(submittedAnswers[i].attributes[1].value);
            }
        }
        //create an array to store the question ID from the Name attribute
        checkedArrName = [];
        //loop through every item in the submittedAnswers object
        for (var i = 0; i < submittedAnswers.length; ++i) {

            //if the radio button is checked, push the name value which stores the quiz question ID
            if (submittedAnswers[i].checked) {
                checkedArrName.push(submittedAnswers[i].name);
            }
        }
        //create an array to store the split id from the name attribute
        split_id_from_str = [];
        //go through all the name attributes and split the id in the string 
        for (var i = 0; i < checkedArrName.length; ++i) {
            var str = checkedArrName[i];
            split_id_from_str.push(str.match(/\d+/g)[0]);
        }
        //Create an array to store the length of how many quiz questions there are using the name attribute which stores the quiz question ID 
        checkedArrNameLength = [];
        //Loop 
        for (var i = 0; i < submittedAnswers.length; ++i) {
                checkedArrNameLength.push(submittedAnswers[i].name);
        }
        let selectUniqueArrayValues = [...new Set(checkedArrNameLength)];

        var num_of_questions_ctr = selectUniqueArrayValues.length;
        //create a counter variable 
        var answerCorrectCtr = 0;
        //loop through the checkedArr array and if the question correct value is equal to the string True(string because it's
        //from the tag attribute), increment the ctr.
        for (var i = 0; i < checkedArr.length; ++i) {
            if (checkedArr[i] == "True") {
            answerCorrectCtr++;
                    }
            }
        if (split_id_from_str.length != num_of_questions_ctr) {
            $('#quizModal-invalid').modal('show');
        } else {
            //if the counter does not match the length of the array, i.e False answers are present, say not correct and highlight answers accordingly
            //else say correct and highlight answers accordingly.
                if (answerCorrectCtr != checkedArr.length) {
                    for (var i = 0; i < checkedArr.length; i++) {
                        for (var j = 0; j < split_id_from_str.length; j++) {
                            if (checkedArr[i] == "True") {
                                document.getElementById("quiz-question" + split_id_from_str[i]).style.backgroundColor = "rgb(198,239,206)";
                            } else {
                                document.getElementById("quiz-question" + split_id_from_str[i]).style.backgroundColor = "rgb(255,199,206)";
                            }
                        }
                    }
                    $('#quizModal-incorrect').modal('show');
                } else {
                    for (var i = 0; i < checkedArr.length; i++) {
                        for (var j = 0; j < split_id_from_str.length; j++) {
                            if (checkedArr[i] == "True") {
                                document.getElementById("quiz-question" + split_id_from_str[i]).style.backgroundColor = "rgb(198,239,206)";
                            }
                        }
                    }
                    $('#quizModal-correct').modal('show');
                }
            }
    }

    //Show profile Pic modal
    function profilePicModal() {
        $('#profilePictureModal').modal('show');
    }
    //Show add friend modal
    function addFriendModal() {
        $('#addFriendModal').modal('show');
    }
    //Show add project modal
    function addProjectModal() {
        $('#addProjectModal').modal('show');
    }
    //Show edit project modal
    function editProjectModal() {
        $('#editProjectModal').modal('show');
    }
        

