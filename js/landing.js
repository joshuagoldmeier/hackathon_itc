class NavBar extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <nav class="navbar navbar-light">
                <a id="brand" href="#">GeaRoBot</a>
                <a id="contact">Contact US</a>
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
                    <h1>Welcome to GeaRoBot</h1>
                    <h3>The Best way to optimize your gear shopping experience <br/>I want to know you a little bit better, click on the button and let's have a little chat together</h3>
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
