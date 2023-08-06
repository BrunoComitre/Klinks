from crypt import methods
import json
import pyodide

from pyodide.http import pyfetch

async def make_request(url, method, body):
    csrf = document.getElementById('csrf_token').value

    headers = {
        'X-Request-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf
    }

    response = await pyfetch(
        url=url,
        method=method,
        body=body,
        headers=headers
    )

    return await response.json()


async def submit_form(e):
    link_input = document.querySelector('#linkInput')
    link = link_input.value

    body = json.dumps({'name': link})

    response = await make_request(url='/', method='POST', body=body)

    if response.get('errors'):
        link_input.classList.add('is-invalid')
    else:
        link_input.classList = 'form-control is-valid'

        ul = document.getElementById('cities')
        li = document.createElement('li') 
        li.innerHTML = response['name']
        ul.appendChild(li)


def main():
    button = document.getElementById('button')
    button.addEventListener('click', pyodide.create_proxy(submit_form))


main()
