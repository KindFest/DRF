import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css'
import UsersList from "./components/UsersList.js"
import ProjectsList from "./components/ProjectsList.js"
import TODOList from "./components/TODOList.js"
import LoginForm from './components/LoginForm.js'
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
            'TODO': [],
            'token': ''
        }
    }

obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {
                'username': login,
                'password': password
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    isAuth() {
        return !!this.state.token
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'users': [] })
            })

        axios
            .get('http://127.0.0.1:8000/api/Projects/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'projects': [] })
            })
        axios
            .get('http://127.0.0.1:8000/api/TODO/', {headers})
            .then(response => {
                const TODOs = response.data.results
                this.setState(
                    {
                        'TODO': TODOs
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'TODO': [] })
            })
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': '',
        }, this.getData)
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
                        <li>
                        {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/users' element={<UsersList users={this.state.users} />} />
                        <Route exact path='/projects' element={<ProjectsList projects={this.state.projects} />} />
                        <Route exact path='/TODO' element={<TODOList TODOs={this.state.TODO} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />

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
