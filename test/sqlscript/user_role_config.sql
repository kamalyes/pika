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
-- Table structure for user_role_config
-- ----------------------------
DROP TABLE IF EXISTS `user_role_config`;
CREATE TABLE `user_role_config`
(
    `id`             int(11) NOT NULL AUTO_INCREMENT COMMENT '角色id',
    `role_name`      varchar(255) NOT NULL COMMENT '角色名称',
    `description`    varchar(255)          DEFAULT NULL COMMENT '备注信息',
    `is_usable`     int(11) DEFAULT '1' COMMENT '禁用/启用 1：启用、0：禁用',
    `create_user_no` varchar(20)           DEFAULT NULL COMMENT '创建者用户编号',
    `update_user_no` varchar(20)           DEFAULT NULL COMMENT '修改者用户编号',
    `create_time`    datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time`    datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COMMENT='角色配置表';

-- ----------------------------
-- Records of user_role_config
-- ----------------------------
INSERT INTO `user_role_config`
VALUES ('1', 'ROOT', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('2', '总监', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('3', '开发', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('4', '测试', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('5', '运维', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('6', '实习生', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('7', '已离职', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
INSERT INTO `user_role_config`
VALUES ('8', '外部未知人员', null, '1', 'SystemSync', 'SystemSync', '2022-01-20 15:00:00', '2022-01-20 15:00:00');
