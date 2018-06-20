
class App extends React.Component{
    constructor(props){
        super(props);
    }
    

    render(){
            return(
                <div>Lets start the app
                    <button><a href="mainpage.html">button</a></button>
                </div>
            
            );
    }

    
}


ReactDOM.render(

    <App/>,
    document.getElementById("root")
);
