import React, { Component } from 'react';

class Test extends Component {
    
    styles = {
        "margin-top":"50px",
        "padding-right":"20px",
        "padding-left":"20px",
        "fontSize" : "100px"
    };

    render() {      
        return(
        <div class = "container">
            <div class="row">
                <div class="but" style = {this.styles}>
                    <button class="btn btn-primary btn-lg" type="button">PDF</button>
                </div>
            </div>
            <div class="row">
                <div class="but" style = {this.styles}>
                    <button class="btn btn-primary btn-lg" type="button">PDF</button>
                </div>
            </div>
            <div class="row">
                <div class="but" style = {this.styles}>
                    <button class="btn btn-primary btn-lg" type="button">PDF</button>
                </div>
            </div>
        </div>
        );
    }
}
 
export default Test;