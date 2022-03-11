
let counter = 0;

  document.querySelector('form').onsubmit =  () => {
       localStorage.setItem(document.querySelector('#order').disabled,true)

        alert('Your room ordered successfully.');
  }

  document.querySelector('#cancel').onclick = () => {
    localStorage.setItem(document.querySelector('#order').disabled,false)
    alert('Ordered room cancelled successfully look for other rooms');
}

