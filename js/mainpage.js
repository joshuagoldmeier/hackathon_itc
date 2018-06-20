// import axios from 'axios';

class MainPage extends React.Component{
    constructor(props){
        super(props); 
        this.getTheItem = this.getTheItem.bind(this)    }

    // componentDidMount() {
    //     axios.get(`http://exmaple.com/blog/${this.props.id}`)
    //       .then(response => this.setState(response.data))
    //   }
    
    render(){
        return(
            <div class="item" > </div>
        )
    }
}

ReactDOM.render(

    <MainPage/>,
    document.getElementById("root")
);