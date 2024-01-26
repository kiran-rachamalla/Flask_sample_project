$("#saveDetails").click(function(){
let data = {
    a: $('input[name="a"]').val(),
    b: $('input[name="b"]').val(),
}
fetch('/saveQuestions', {
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "body": JSON.stringify(data),
}).then(response => response.json())
    .then(data1 => {
        $( "div.container" ).replaceWith( data1.success );
    })
  });