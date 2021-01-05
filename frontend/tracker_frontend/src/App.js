import React from "react";
import "./App.css";
import Users from "./components/userDetail";
import Nav from "./components/Navigation";
import Login from "./components/Login"
import SimpleMap from "./components/maps";
import Home from "./components/Home";
import Registration from "./components/Registration"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
//import RecipesList from "./components/RecipesList";




function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path="/" exact component={Home} />
          {/* <Route path="/login" component={Login} /> */}
          {/* <Route path="/users" exact component={Users}/>  */}
          <Route path="/location" component={SimpleMap}/>
          {/* <Route path="/registration" component={Registration}/> */}
        </Switch>
      </div>
    </Router>
  );
}
export default App;
