#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/filter_indices.h>
#include <pcl/point_cloud.h>
#include <pcl/visualization/pcl_visualizer.h>

using namespace std;

int main()
{

//***************************read PCD file*****************************************
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);

    //加载文件
    if (pcl::io::loadPCDFile<pcl::PointXYZ>("/home/marco/文档/Lidar_data/bunny2.pcd", *cloud) == -1){
        std::cerr << "open failed!" << std::endl;
        return -1;
    }


    boost::shared_ptr< pcl::visualization::PCLVisualizer > viewer(new pcl::visualization::PCLVisualizer("Viewer"));
    viewer->setBackgroundColor(0, 0, 0);//这个是RGB,0,0,0是黑色.255,255,255是白色.
    int vp;
    viewer->createViewPort(0.0, 0.0, 1.0, 1.0, vp);//设置窗口视点.
    pcl::visualization::PointCloudColorHandlerCustom<pcl::PointXYZ> source_color(cloud, 0, 255, 0);
    viewer->addPointCloud<pcl::PointXYZ>(cloud, source_color, "s", vp);
    viewer->setPointCloudRenderingProperties(pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 2, "source");
    viewer->spin();
}
