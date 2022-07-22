/*
Navicat MySQL Data Transfer

Source Server         : 腾讯云
Source Server Version : 50735
Source Host           : localhost:3306
Source Database       : auto_test

Target Server Type    : MYSQL
Target Server Version : 50735
File Encoding         : 65001

Date: 2022-01-20 09:55:38
*/

SET
FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for permission_control
-- ----------------------------
DROP TABLE IF EXISTS `permission_control`;
CREATE TABLE `permission_control`
(
    `id`             int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
    `control_id`     int(11) NOT NULL COMMENT '权限控制id',
    `description`    varchar(20) NOT NULL COMMENT '权限控制说明',
    `create_user_no` varchar(20)          DEFAULT '' COMMENT '创建者用户编号',
    `update_user_no` varchar(20)          DEFAULT '' COMMENT '修改者用户编号',
    `create_date`    datetime    NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
    `update_date`    datetime    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日期',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COMMENT='权限控制表';

-- ----------------------------
-- Records of permission_control
-- ----------------------------
INSERT INTO `permission_control`
VALUES ('1', '1', 'ROOT', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
INSERT INTO `permission_control`
VALUES ('2', '2', 'INSERT_ONLY', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
INSERT INTO `permission_control`
VALUES ('3', '3', 'DELETE_ONLY', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
INSERT INTO `permission_control`
VALUES ('4', '4', 'UPDATE_ONLY', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
INSERT INTO `permission_control`
VALUES ('5', '5', 'SELECT_ONLY', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
INSERT INTO `permission_control`
VALUES ('6', '6', 'SELECT_AND_INSERT', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
INSERT INTO `permission_control`
VALUES ('7', '7', 'SELECT_AND_UPDATE', 'SystemSync', 'SystemSync', '2022-01-20 19:06:55', '2022-01-20 19:06:55');
