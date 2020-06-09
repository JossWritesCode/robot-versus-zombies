import React from "react";
import SignIn from "./SignIn";
import SignUp from "./SignUp";
import Main from "./Main";
import { BrowserRouter as Router } from "react-router-dom";
import { Switch, Route } from "react-router-dom";
import theme from "./ui/theme";
import { ThemeProvider } from "@material-ui/core/styles";
function App() {
  return (
    <Router>
      <ThemeProvider theme={theme}>
        <Switch>
          <Route exact path="/">
            <Main />
          </Route>
          <Route exact path="/signin">
            <SignIn />
          </Route>
          <Route exact path="/signup">
            <SignUp />
          </Route>
        </Switch>
      </ThemeProvider>
    </Router>
  );
}

export default App;
