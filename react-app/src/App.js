import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const isAuthenticated = Boolean(user);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);


  // Hide Navigation component on /login page
  const showNavigation = location.pathname !== '/login' && user;

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/login">
          {isAuthenticated ? (
            <Redirect to="/" />
          ) : (
            <LoginFormPage />
          )}
          </Route>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          {/* Redirect unauthenticated users to login page */}
          <Route>
            <Redirect to="/login" />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
