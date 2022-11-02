window.addEventListener("load", function ()
{
    //Get click element references.
    let clickCounterElement = document.getElementById("click-counter");
    let clcikButtonElement = document.getElementById("click-button");

    //Counter value.
    let counter = 0;

    //Cliclk button function.
    let clickButtonFunction = function ()
    {
        //Increment counter
        counter++;

        //Update counter value
        clickCounterElement.innerHTML = counter;
    };

    //Attach button function.
    clcikButtonElement.addEventListener("click", clickButtonFunction);
});