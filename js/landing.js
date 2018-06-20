class NavBar extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <nav class="navbar navbar-light">
                <a class="navbar-brand" href="#">
                    <img src="/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt=""/>
                        GeaRoBot
                </a>
            </nav>
        );
    }
}


class Menu extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div>
            <button id ="btn-menu" type="button" class="btn btn-primary btn-lg"><a href="boto">GET STARTED</a></button>
            </div>
        )
    }
}


class Footer extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div class="container">
                <a href="https://www.facebook.com" class="fa fa-facebook-official"/>
                <a href="https://twitter.com" class="fa fa-twitter"/>
            </div>
        )
    }
}


class App extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
            return(
                <div>
                    <NavBar/>
                    <h1>Welcome to our Site</h1>
                    <h3>Here you can choose your favorite sport and get shopping advices according to your level</h3>
                    <Menu/>
                    <Footer/>
                </div>
            );
    }
}

ReactDOM.render(

    <App/>,
    document.getElementById("root")
);
