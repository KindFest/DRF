import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css'
import UsersList from "./components/UsersList.js"
import ProjectsList from "./components/ProjectsList.js"
import TODOList from "./components/TODOList.js"
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'

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
            'users': [],
            'projects': [],
            'TODO': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/Projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/TODO/')
            .then(response => {
                const TODOs = response.data.results
                this.setState(
                    {
                        'TODO': TODOs
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return(
            <div>
                {/*<UsersList users={this.state.users} />*/}
                <BrowserRouter>
                    <nav>
                        <li> <Link to='/users' >Users</Link> </li>
                        <li> <Link to='/Projects' >Projects</Link> </li>
                        <li> <Link to='/TODO' >TODOs</Link> </li>
                    </nav>

                    <Routes>
                        <Route exact path='/users' element={<UsersList users={this.state.users} />} />
                        <Route exact path='/projects' element={<ProjectsList projects={this.state.projects} />} />
                        <Route exact path='/TODO' element={<TODOList TODOs={this.state.TODO} />} />

                    </Routes>
                </BrowserRouter>
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
