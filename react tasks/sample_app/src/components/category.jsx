const Category=()=>{

        const name=['nishanth','nani','nishu']
        const arryobj=[{name:'pip',age:20},{name:'vicky',age:25},{namw:'ram',age:15}]

        return <div>
            {name.map((value,index)=><p key={index}> name is {value}</p>)}
            {arryobj.map((value,index)=><h1 key={index}>name is {value.name} age is {value.age}</h1>)}
        </div>
}
export default Category