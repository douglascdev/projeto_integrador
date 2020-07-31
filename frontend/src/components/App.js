import React, { Component } from "react";
import { render } from "react-dom";
import MenuAppBar from "./MenuAppBar";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Carregando..."
    };
  }

  componentDidMount() {
    // fetch("cadastro/caminhao")
    //   .then(response => {
    //     if (response.status > 400) {
    //       return this.setState(() => {
    //         return { placeholder: "Não foi possível carregar o cadastro!" };
    //       });
    //     }
    //     return response.json();
    //   })
    //   .then(data => {
    //     this.setState(() => {
    //       return {
    //         data,
    //         loaded: true
    //       };
    //     });
    //   });
  }

  render() {
    return (
        <MenuAppBar/>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);