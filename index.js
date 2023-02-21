
/* window.addEventListener("load", (event) => {
// Make a GET request to the website URL using the Fetch API
fetch('https://partyflock.nl/agenda')
  .then((response) => {
    // Convert the response to a text format
    return response.text();
  })
  .then((html) => {
    // Create a new DOM object from the HTML text
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    // Get all the 'a' tags that have an 'href' attribute
    const links = Array.from(doc.querySelectorAll('a[href]'))
      .map((a) => a.getAttribute('href'))
      .filter((href) => href.match(/^\/party\/\d+$/));

    // Print the links
    console.log(links);
  })
  .catch((error) => {
    console.log(error);
  });

  
  });


  let mapOptions = {
    center:[51.958, 9.141],
    zoom:10
} */

function show_event(){
  console.log(123)


}