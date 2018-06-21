
class MainPage extends React.Component{
    constructor(props){
        super(props); 
        this.getItem =this.getItem.bind(this)
        var cookieSplitted = document.cookie.split(";");
        this.state={
            name: cookieSplitted[1].substring(6),
            sport : cookieSplitted[0].substring(7)
        }
    }

    componentDidMount() {
        this.getItem();
     }

    getItem(){
       
        $.ajax({
            type:"GET",
            url:"/sports/ski",
            
            dataType:"json",
            success: function (response){
                // var item =[Name,Price,URL,Description,Image,Size];
                var counter = 0
                var row = $("<div>")
                row.addClass("row")
                console.log(response)
               for (var i = 0 ; i<Object.keys(response).length ; i++){

                   if (counter<2){
                        counter++;
                        var product =$("<div>")
                        product.addClass("col-6 product")
                        product.append("name: "+Object.values(response)[i].Name+"</br>")

                        product.append("price: "+Object.values(response)[i].Price+"$"+"</br>")

                        var link=$("<a>")
                        link.attr("target","_new")
                        link.attr("href",Object.values(response)[i].URL)
                        link.append("link to the product");
                        link.append("</br>")

                        product.append(link)

                        product.append("Description: "+Object.values(response)[0].Description+"</br>")
                       

                        product.append("color: "+Object.values(response)[0].Size+"</br>")
                        var image= $("<img>");

                        image.addClass("product-image")
                        image.attr("src",Object.values(response)[i].Image+"</br>")
                        image.appendTo(product) 
                        product.appendTo(row);   
                   }
                   else{
                        row.appendTo($(".items"));
                       counter = 0;
                       var row = $("<div>")
                       row.addClass("row")
                       var product =$("<div>")
                       product.addClass("col-6 product")
                       counter++;
                       var product =$("<div>")
                       product.addClass("col-6 product")
                       product.append("name: "+Object.values(response)[i].Name+"</br>")

                       product.append("price: "+Object.values(response)[i].Price+"$"+"</br>")

                       var link=$("<a>")
                       link.attr("target","_new")
                       link.attr("href",Object.values(response)[i].URL)
                       link.append("link to the product");
                       link.append("</br>")

                       product.append(link)

                       product.append("Description: "+Object.values(response)[0].Description+"</br>")
                      

                       product.append("color: "+Object.values(response)[0].Size+"</br>")
                       var image= $("<img>");

                       image.addClass("product-image")
                       image.attr("src",Object.values(response)[i].Image+"</br>")
                       image.appendTo(product) 
                       product.appendTo(row); 
                       
                       counter++;
                       
                   }
               }
               row.appendTo($(".items")); 
            },
            
            error: function(msg){
                console.log("error");
            },
    
        });
    }
    render(){
        return(
            <div className= "maincontainer">
                <h1>Hi <span>{this.state.name} </span><img id="headimg" src="../images/frobot.png"/> have found the best deals for you</h1>
                <div className="displayBy">
                    <div className="container">
                        <div className="row">
                            <button className="col-6">Display By Rates</button>
                            <button className="col-6">Display By Prices</button>
                        </div>
                    </div>
                </div>
                <div className="items container"></div>
            </div>
        )
    }
}

ReactDOM.render(

    <MainPage/>,
    document.getElementById("root")
);