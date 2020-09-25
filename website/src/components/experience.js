
import * as echarts from 'echarts';
import * as Data from '../dist/experience.json';
export default function () {

    var myChart = echarts.init(document.getElementById('experience'));
    var series =  Data['data'].map((item,index)=>{
        return {value:item,name:Data['index'][index]}
    })
    // 指定图表的配置项和数据
    var option  = {
        title: {
            text: '经验',
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },

        series: [
            {
                type: 'pie',
                radius: '40%',
                center: ['50%', '50%'],
                data: series,

            }
        ]
    };


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    console.log(myChart)
}
