# Designing Your Front-end For A Custom Page

> This page is still under construction ⚠️

We want to provide you the steps to build a custom component, however, we plan to signficantly re-write this part of the documentation to provide in-depth details. For now, it is the absolute bare-minimum to get started.

## 1. Create your react.js file

In `react/src/` create a new `.js` file.

Here's an example:

```javascript
import React from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';


// A simple Page example
class Page extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    // Every component should do this!
    componentDidMount() {

        // Get the URL
        const url = window.location.href.split('?')[0]; 

        // Request the `/init` route
        axios.get(url+ "/init").then(res => {

            // Set the react state dict from the backend state dict
            this.setState(res.data);
        })      
    }

    // Render your custom page here
    render() {
      if (this.state.pipeline == undefined) return <p>Loading...</p>;      
      const data = this.state.pipeline[0].data;
      return (
        <div>            
            <h1>{data.title}</h1>            
            <p>{data.description}</p>
            <Button onClick={this.popComponent} variant="contained" color="primary">{data.button_name}</Button>            
        </div>
      );
    }    

    // Add some custom logic here
    popComponent = () => {

        // Here is how you send an instruction to the backend
        const url = window.location.href.split('?')[0];            
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'advance'})).then(res => {
            this.setState(res.data); // Make sure to update the front-end state dict with the result        
            this.props.advance();             
        })
    }
}

// Don't forget to export your page
export default Page;
```

## 2. Import your new react page in `Start.js`

In `react_app/src/Start.js`, follow the instructions there:

```javascript

// Start.js

// 1. Import your new components here!
import Page from './Page';
// ...

// 2. Add 'case' in the render() function
render() {      
    return (
    <div>
        {(() => {
        
        if (this.state.pipeline == undefined) return <p>Loading...</p>;

        const name = this.state.pipeline[0].name; 
        
        switch (name) {

            // Add your new page here!
            case 'Page':
            return <Page advance={this.getLatestState}/>;

            // ...

            // Add more components here :)

            default:
            return <p>Unknown component!</p>;
        }
        })()}
    </div>
    );
}
```

