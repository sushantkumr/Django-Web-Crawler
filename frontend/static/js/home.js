function submitBytecode() {
    showBusyState();
	let input = $('input#inputUrl').val();
	let data = {
                urlData: input
            };

    url = 'api/?url=' + input;

    $.ajax({
        method: 'POST',
        contentType: 'application/json',
        url: url,
        success: function (response) {
            if (response.success) {
                let output = response.data;
                $('textarea#outputArea').val(output);
                removeBusyState();
            }
            else {
                console.log('Error: ' + response.message);
            }
        },
        error: function(a, b, c) {
            console.log(a, b, c);
        }
    });

};

function clearTextArea() {
    $('input#inputUrl').val("");
    $('textarea#outputArea').val("");
};

function showBusyState() {
    $("#busyMessage").removeClass("hidden");
    $("#submitInput").addClass("loading");
}

function removeBusyState() {
    $("#busyMessage").addClass("hidden");
    $("#submitInput").removeClass("loading");
}
