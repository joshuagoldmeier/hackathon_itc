class MainPage extends React.Component{
    constructor(props){
        super(props);  
    }

    render(){
        return(
            <div> MainPage works!</div>
        )
    }
}

ReactDOM.render(

    <MainPage/>,
    document.getElementById("root")
);