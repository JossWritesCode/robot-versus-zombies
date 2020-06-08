import { createMuiTheme } from "@material-ui/core/styles";

const celadonGreen = "#C9E265";
const spaceCadet = "#2F2D59";
const nightBlue = "#297495";

export default createMuiTheme({
  palette: {
    common: {
      celadonGreen: `${celadonGreen}`,
      spaceCadet: `${spaceCadet}`,
      nightBlue: `${nightBlue}`,
    },
    primary: {
      main: `${celadonGreen}`,
    },
    secondary: {
      main: `${spaceCadet}`,
    },
  },
});
