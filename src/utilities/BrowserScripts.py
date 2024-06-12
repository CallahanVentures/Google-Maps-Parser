parseBusinessLinksScript = """function parseMapsForBusinessLinks() {
    var htmlContent = document.documentElement.innerHTML;
    var tempElement = document.createElement('div');
    tempElement.innerHTML = htmlContent;
    
    // Find all <a> elements with hrefs containing "https://www.google.com/maps/place/"
    var googleMapsLinks = [];
    var allLinks = tempElement.querySelectorAll('a');
    allLinks.forEach(function(link) {
        var href = link.getAttribute('href');
        if (href && href.includes('https://www.google.com/maps/place/')) {
            googleMapsLinks.push(href);
        }
    });
    
    return googleMapsLinks;
}

    

// Call the function when you're ready to execute its functionality
return parseMapsForBusinessLinks();"""

parseBusinessNameScript = """function getBusinessName(){
    var htmlContent = document.documentElement.innerHTML;
    var tempElement = document.createElement('div');
    tempElement.innerHTML = htmlContent;

    // Find the specific div based on padding-bottom style
    var targetDiv = Array.from(tempElement.querySelectorAll('div')).find(div => {
        var paddingBottom = div.style.paddingBottom;
        return paddingBottom && paddingBottom === '4px';
    });

    // Check if the div exists
    if (targetDiv) {
        // Find the h1 element within the target div
        var h1Element = targetDiv.querySelector('h1');

        // Check if the h1 element exists
        if (h1Element) {
            // Get the text content of the h1 element
            var businessName = h1Element.textContent.trim();

            // Output the business name
            console.log('Business Name:', businessName);
            return businessName;

        } 
        else { return "Not Found"; } } 
    
    else { return "Not Found"; }
}"""

parseBusinessAddressScript = """function getBusinessAddress(){
    var htmlContent = document.documentElement.innerHTML;
    var tempElement = document.createElement('div');
    tempElement.innerHTML = htmlContent;
    
    // Find the button with data-tooltip="Copy address"
    var targetButton = tempElement.querySelector('button[data-tooltip="Copy address"]');

    // Check if the button exists
    if (targetButton) {
        // Find all divs within the button
        var divs = targetButton.getElementsByTagName('div');
    
        // Iterate through the divs
        for (var i = 0; i < divs.length; i++) {
            var divText = divs[i].textContent.trim();
            // Check if the div text doesn't contain the unicode character
            if (!divText.includes('')) {
                console.log('Found div with text:', divText);
                break; // Stop searching after finding the first suitable div
            }
        }

        if(divText){ return divText; }
        return "Not Found";
    } 
    else { return "Not Found"; }
}"""

parseBusinessPhoneScript = """function getBusinessPhone(){
    var htmlContent = document.documentElement.innerHTML;
    var tempElement = document.createElement('div');
    tempElement.innerHTML = htmlContent;

    // Find the button with data-tooltip="Copy phone number"
    var targetButtonPhone = tempElement.querySelector('button[data-tooltip="Copy phone number"]');

    if (targetButtonPhone) {

        // Finds all divs within the button tag
        var divsPhone = targetButtonPhone.getElementsByTagName('div');

        // Iterates through the button's divs & stops searching after finding the first div text matching criteria
        for (var j = 0; j < divsPhone.length; j++) {
            var divTextPhone = divsPhone[j].textContent.trim();
            if (!divTextPhone.includes('')) {
                return divTextPhone;
            }
        }
    } 
    else { return "Not Found"; }
}"""

parseBusinessWebsiteScript = """function getBusinessWebsite() {
    var htmlContent = document.documentElement.innerHTML;

    // Create a temporary element to parse the HTML content
    var tempElement = document.createElement('div');
    tempElement.innerHTML = htmlContent;

    // Find the link with data-tooltip="Open website"
    var targetLinkWebsite = tempElement.querySelector('a[data-tooltip="Open website"]');

    // Check if the link exists
    if (targetLinkWebsite) {
        var websiteURL = targetLinkWebsite.getAttribute('href');
        return websiteURL;
    } else {
        return null;
    }
}"""
