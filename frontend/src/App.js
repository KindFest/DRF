import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css'
import UsersList from "./components/UsersList.js"

class Menu extends React.Component {
    render() {
        return(
            <div>
                Menu
            </div>
        )
    }
}

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return(
            <div>
                <UsersList users={this.state.users} />
            </div>
        )
    }
}

class Footer extends React.Component {
    render() {
        return(
            <div>
                Footer
            </div>
        )
    }
}

export {App, Menu, Footer};
