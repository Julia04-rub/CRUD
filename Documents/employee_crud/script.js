const API = "/employees"
const token = localStorage.getItem("token")


if(!token){
    window.location = "login.html"
}

let currentId = null

function logout(){

    localStorage.removeItem("token")

    window.location = "login.html"

}

async function fetchEmployees(){

    const res = await fetch(API,{
        headers:{
            Authorization: "Bearer " + token
        }
    })

    const data = await res.json()

    const table = document.getElementById("employeeTable")
    table.innerHTML = ""

    data.forEach(emp => {

        table.innerHTML += `
        <tr>
            <td>${emp.id}</td>
            <td>${emp.name}</td>
            <td>${emp.position}</td>
            <td>${emp.salary}</td>

            <td>

                <button class="edit-btn"
                onclick="editEmployee(${emp.id},'${emp.name}','${emp.position}',${emp.salary})">
                <i class="fa-solid fa-pen-to-square"></i>
                </button>

                <button class="delete-btn"
                onclick="deleteEmployee(${emp.id})">
                <i class="fa-solid fa-delete-left"></i>
                </button>

            </td>

        </tr>
        `
    })
}




async function addEmployee(){

    const name = document.getElementById("name").value
    const position = document.getElementById("position").value
    const salary = document.getElementById("salary").value


   
    if(currentId){

        await fetch(API + "/" + currentId,{
            method:"PUT",
            headers:{
                "Content-Type":"application/json",
                Authorization:"Bearer " + token
            },
            body: JSON.stringify({name,position,salary})
        })

        currentId = null

    }else{

        
        await fetch(API,{
            method:"POST",
            headers:{
                "Content-Type":"application/json",
                Authorization:"Bearer " + token
            },
            body: JSON.stringify({name,position,salary})
        })

    }



    document.getElementById("name").value = ""
    document.getElementById("position").value = ""
    document.getElementById("salary").value = ""

    fetchEmployees()
}




function editEmployee(id,name,position,salary){

    document.getElementById("name").value = name
    document.getElementById("position").value = position
    document.getElementById("salary").value = salary

    currentId = id
}




async function deleteEmployee(id){

    await fetch(API + "/" + id,{
        method:"DELETE",
        headers:{
            Authorization:"Bearer " + token
        }
    })

    fetchEmployees()
}




fetchEmployees()