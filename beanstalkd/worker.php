<?php
/**
 * Created by PhpStorm.
 * User: jeevi
 * Date: 2016/10/29
 * Time: 22:49
 */
namespace  worker;

use Pheanstalk\Pheanstalk;


require_once (__DIR__."/vendor/autoload.php");
$pheanstalk = new Pheanstalk('127.0.0.1','11300');

echo "stats:".PHP_EOL;
var_dump($pheanstalk->stats());
echo PHP_EOL;
$job = $pheanstalk
    ->watch('testtube')
    ->ignore('default')
    ->reserve();
echo "getData:".PHP_EOL;
echo $job->getData();

echo PHP_EOL."status:".PHP_EOL;
var_dump($pheanstalk->getConnection()->isServiceListening()); // true or false

//$pheanstalk->delete($job);