import { createMuiTheme } from "@material-ui/core/styles";

const celadonGreen = "#C9E265";
const spaceCadet = "#2F2D59";
const nightBlue = "#297495";
const black = "#02111b";

export default createMuiTheme({
  palette: {
    common: {
      celadonGreen: `${celadonGreen}`,
      spaceCadet: `${spaceCadet}`,
      nightBlue: `${nightBlue}`,
      black: `${black}`,
      white: "white",
    },
    primary: {
      main: `${celadonGreen}`,
    },
    secondary: {
      main: `${spaceCadet}`,
    },
  },
});
